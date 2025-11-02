"""
GUI Calculator mimicking Casio FX-991 CN X.
Cross-platform GUI using tkinter.
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import math
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from calculator_engine import CalculatorEngine


class CasioCalculatorGUI:
    """Main GUI calculator class."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Casio FX-991 CN X Calculator")
        self.root.geometry("500x700")
        self.root.resizable(True, True)
        
        self.engine = CalculatorEngine()
        self.current_input = ""
        self.history = []
        
        # Configure style
        self.setup_style()
        
        # Create UI
        self.create_display()
        self.create_mode_selector()
        self.create_button_panel()
        self.create_menu()
        
    def setup_style(self):
        """Setup GUI styling."""
        style = ttk.Style()
        style.theme_use('clam')
        
    def create_menu(self):
        """Create menu bar."""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Clear History", command=self.clear_history)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Mode menu
        mode_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Mode", menu=mode_menu)
        mode_menu.add_command(label="Degree", command=lambda: self.set_angle_mode('deg'))
        mode_menu.add_command(label="Radian", command=lambda: self.set_angle_mode('rad'))
        mode_menu.add_command(label="Grad", command=lambda: self.set_angle_mode('grad'))
        
        # Tools menu
        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Equation Solver", command=self.open_equation_solver)
        tools_menu.add_command(label="Function Grapher", command=self.open_graph_window)
        tools_menu.add_command(label="Statistics", command=self.open_statistics)
        tools_menu.add_command(label="Base Converter", command=self.open_base_converter)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
        help_menu.add_command(label="Help", command=self.show_help)
        
    def create_display(self):
        """Create display area."""
        display_frame = ttk.Frame(self.root, padding="10")
        display_frame.pack(fill=tk.BOTH, expand=False)
        
        # History display
        history_label = ttk.Label(display_frame, text="History:", font=('Arial', 9))
        history_label.pack(anchor=tk.W)
        
        self.history_display = scrolledtext.ScrolledText(
            display_frame, height=4, width=50, 
            font=('Courier', 9), state=tk.DISABLED
        )
        self.history_display.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Main display
        self.display = tk.Entry(
            display_frame, font=('Arial', 16), 
            justify=tk.RIGHT, bg='#e8f5e9'
        )
        self.display.pack(fill=tk.X, pady=5)
        self.display.insert(0, "0")
        
        # Result display
        self.result_display = tk.Entry(
            display_frame, font=('Arial', 14, 'bold'), 
            justify=tk.RIGHT, bg='#c8e6c9', state='readonly'
        )
        self.result_display.pack(fill=tk.X)
        
    def create_mode_selector(self):
        """Create mode selector."""
        mode_frame = ttk.Frame(self.root, padding="5")
        mode_frame.pack(fill=tk.X)
        
        ttk.Label(mode_frame, text="Angle Mode:").pack(side=tk.LEFT, padx=5)
        
        self.angle_mode_var = tk.StringVar(value="deg")
        modes = [("Deg", "deg"), ("Rad", "rad"), ("Grad", "grad")]
        
        for text, mode in modes:
            ttk.Radiobutton(
                mode_frame, text=text, variable=self.angle_mode_var,
                value=mode, command=lambda m=mode: self.set_angle_mode(m)
            ).pack(side=tk.LEFT, padx=5)
        
    def create_button_panel(self):
        """Create calculator buttons."""
        button_frame = ttk.Frame(self.root, padding="10")
        button_frame.pack(fill=tk.BOTH, expand=True)
        
        # Button layout inspired by Casio FX-991
        buttons = [
            ['shift', 'mode', 'clear', 'del', '(', ')'],
            ['x²', '√', '^', 'log', 'ln', '÷'],
            ['sin', 'cos', 'tan', '7', '8', '9', '×'],
            ['sin⁻¹', 'cos⁻¹', 'tan⁻¹', '4', '5', '6', '−'],
            ['x!', 'abs', 'π', '1', '2', '3', '+'],
            ['Ans', 'e', 'exp', '0', '.', '='],
        ]
        
        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                btn = tk.Button(
                    button_frame, text=btn_text,
                    font=('Arial', 10, 'bold'),
                    width=6, height=2,
                    command=lambda t=btn_text: self.on_button_click(t)
                )
                
                # Color coding
                if btn_text in ['=']:
                    btn.config(bg='#4CAF50', fg='white')
                elif btn_text in ['clear', 'del']:
                    btn.config(bg='#f44336', fg='white')
                elif btn_text in ['+', '−', '×', '÷', '^']:
                    btn.config(bg='#FF9800', fg='white')
                elif btn_text in ['shift', 'mode']:
                    btn.config(bg='#2196F3', fg='white')
                elif btn_text.isdigit() or btn_text == '.':
                    btn.config(bg='#e0e0e0')
                else:
                    btn.config(bg='#f5f5f5')
                
                btn.grid(row=i, column=j, padx=2, pady=2, sticky='nsew')
            
            # Configure row weights
            button_frame.grid_rowconfigure(i, weight=1)
        
        # Configure column weights
        for j in range(max(len(row) for row in buttons)):
            button_frame.grid_columnconfigure(j, weight=1)
    
    def on_button_click(self, button_text):
        """Handle button clicks."""
        current = self.display.get()
        
        if current == "0" and button_text.isdigit():
            current = ""
        
        if button_text == 'clear':
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")
            self.update_result("")
        elif button_text == 'del':
            if len(current) > 1:
                self.display.delete(len(current)-1, tk.END)
            else:
                self.display.delete(0, tk.END)
                self.display.insert(0, "0")
        elif button_text == '=':
            self.calculate()
        elif button_text == 'shift':
            messagebox.showinfo("Shift", "Use menu for advanced functions")
        elif button_text == 'mode':
            self.open_mode_dialog()
        elif button_text in ['sin', 'cos', 'tan', 'sin⁻¹', 'cos⁻¹', 'tan⁻¹']:
            func_map = {
                'sin': 'sin(', 'cos': 'cos(', 'tan': 'tan(',
                'sin⁻¹': 'asin(', 'cos⁻¹': 'acos(', 'tan⁻¹': 'atan('
            }
            self.display.insert(tk.END, func_map[button_text])
        elif button_text == 'x²':
            self.display.insert(tk.END, '**2')
        elif button_text == '√':
            self.display.insert(tk.END, 'sqrt(')
        elif button_text == '^':
            self.display.insert(tk.END, '**')
        elif button_text == 'log':
            self.display.insert(tk.END, 'log(')
        elif button_text == 'ln':
            self.display.insert(tk.END, 'ln(')
        elif button_text == 'x!':
            self.display.insert(tk.END, 'factorial(')
        elif button_text == 'abs':
            self.display.insert(tk.END, 'abs(')
        elif button_text == 'exp':
            self.display.insert(tk.END, 'exp(')
        elif button_text == '÷':
            self.display.insert(tk.END, '/')
        elif button_text == '×':
            self.display.insert(tk.END, '*')
        elif button_text == '−':
            self.display.insert(tk.END, '-')
        elif button_text == 'π':
            self.display.insert(tk.END, 'pi')
        elif button_text == 'e':
            self.display.insert(tk.END, 'e')
        elif button_text == 'Ans':
            self.display.insert(tk.END, 'Ans')
        else:
            self.display.insert(tk.END, button_text)
        
        self.current_input = self.display.get()
    
    def calculate(self):
        """Calculate the expression."""
        try:
            expression = self.display.get()
            result = self.engine.evaluate(expression)
            
            # Format result
            if isinstance(result, complex):
                if result.imag == 0:
                    result_str = f"{result.real:.10g}"
                else:
                    result_str = f"{result.real:.10g} + {result.imag:.10g}i"
            else:
                result_str = f"{result:.10g}"
            
            self.update_result(result_str)
            self.add_to_history(f"{expression} = {result_str}")
            
        except Exception as e:
            self.update_result(f"Error: {str(e)}")
            messagebox.showerror("Calculation Error", str(e))
    
    def update_result(self, text):
        """Update result display."""
        self.result_display.config(state='normal')
        self.result_display.delete(0, tk.END)
        self.result_display.insert(0, text)
        self.result_display.config(state='readonly')
    
    def add_to_history(self, entry):
        """Add calculation to history."""
        self.history.append(entry)
        self.history_display.config(state=tk.NORMAL)
        self.history_display.insert(tk.END, entry + "\n")
        self.history_display.see(tk.END)
        self.history_display.config(state=tk.DISABLED)
    
    def clear_history(self):
        """Clear calculation history."""
        self.history = []
        self.history_display.config(state=tk.NORMAL)
        self.history_display.delete(1.0, tk.END)
        self.history_display.config(state=tk.DISABLED)
    
    def set_angle_mode(self, mode):
        """Set angle mode."""
        self.engine.set_angle_mode(mode)
        self.angle_mode_var.set(mode)
        messagebox.showinfo("Angle Mode", f"Angle mode set to {mode.upper()}")
    
    def open_mode_dialog(self):
        """Open mode selection dialog."""
        dialog = tk.Toplevel(self.root)
        dialog.title("Mode Selection")
        dialog.geometry("250x150")
        
        ttk.Label(dialog, text="Select Angle Mode:", font=('Arial', 12)).pack(pady=10)
        
        for mode_name, mode_val in [("Degree", "deg"), ("Radian", "rad"), ("Grad", "grad")]:
            btn = ttk.Button(
                dialog, text=mode_name,
                command=lambda m=mode_val: [self.set_angle_mode(m), dialog.destroy()]
            )
            btn.pack(pady=5, padx=20, fill=tk.X)
    
    def open_equation_solver(self):
        """Open equation solver window."""
        solver_window = tk.Toplevel(self.root)
        solver_window.title("Equation Solver")
        solver_window.geometry("400x500")
        
        notebook = ttk.Notebook(solver_window)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Linear equation tab
        linear_frame = ttk.Frame(notebook)
        notebook.add(linear_frame, text="Linear (ax+b=0)")
        
        ttk.Label(linear_frame, text="ax + b = 0", font=('Arial', 12, 'bold')).pack(pady=10)
        
        ttk.Label(linear_frame, text="a:").pack()
        a_linear = ttk.Entry(linear_frame)
        a_linear.pack(pady=5)
        
        ttk.Label(linear_frame, text="b:").pack()
        b_linear = ttk.Entry(linear_frame)
        b_linear.pack(pady=5)
        
        result_linear = tk.Text(linear_frame, height=4, width=40)
        result_linear.pack(pady=10)
        
        def solve_linear():
            try:
                a = float(a_linear.get())
                b = float(b_linear.get())
                x = self.engine.solve_linear(a, b)
                result_linear.delete(1.0, tk.END)
                result_linear.insert(tk.END, f"Solution:\nx = {x:.10g}")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        ttk.Button(linear_frame, text="Solve", command=solve_linear).pack(pady=5)
        
        # Quadratic equation tab
        quad_frame = ttk.Frame(notebook)
        notebook.add(quad_frame, text="Quadratic (ax²+bx+c=0)")
        
        ttk.Label(quad_frame, text="ax² + bx + c = 0", font=('Arial', 12, 'bold')).pack(pady=10)
        
        ttk.Label(quad_frame, text="a:").pack()
        a_quad = ttk.Entry(quad_frame)
        a_quad.pack(pady=5)
        
        ttk.Label(quad_frame, text="b:").pack()
        b_quad = ttk.Entry(quad_frame)
        b_quad.pack(pady=5)
        
        ttk.Label(quad_frame, text="c:").pack()
        c_quad = ttk.Entry(quad_frame)
        c_quad.pack(pady=5)
        
        result_quad = tk.Text(quad_frame, height=6, width=40)
        result_quad.pack(pady=10)
        
        def solve_quadratic():
            try:
                a = float(a_quad.get())
                b = float(b_quad.get())
                c = float(c_quad.get())
                x1, x2 = self.engine.solve_quadratic(a, b, c)
                result_quad.delete(1.0, tk.END)
                result_quad.insert(tk.END, f"Solutions:\n")
                if isinstance(x1, complex):
                    result_quad.insert(tk.END, f"x₁ = {x1.real:.10g} + {x1.imag:.10g}i\n")
                    result_quad.insert(tk.END, f"x₂ = {x2.real:.10g} + {x2.imag:.10g}i")
                else:
                    result_quad.insert(tk.END, f"x₁ = {x1:.10g}\n")
                    result_quad.insert(tk.END, f"x₂ = {x2:.10g}")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        ttk.Button(quad_frame, text="Solve", command=solve_quadratic).pack(pady=5)
        
        # Cubic equation tab
        cubic_frame = ttk.Frame(notebook)
        notebook.add(cubic_frame, text="Cubic (ax³+bx²+cx+d=0)")
        
        ttk.Label(cubic_frame, text="ax³ + bx² + cx + d = 0", font=('Arial', 12, 'bold')).pack(pady=10)
        
        for label in ['a:', 'b:', 'c:', 'd:']:
            ttk.Label(cubic_frame, text=label).pack()
            entry = ttk.Entry(cubic_frame)
            entry.pack(pady=2)
            if label == 'a:':
                a_cubic = entry
            elif label == 'b:':
                b_cubic = entry
            elif label == 'c:':
                c_cubic = entry
            else:
                d_cubic = entry
        
        result_cubic = tk.Text(cubic_frame, height=8, width=40)
        result_cubic.pack(pady=10)
        
        def solve_cubic():
            try:
                a = float(a_cubic.get())
                b = float(b_cubic.get())
                c = float(c_cubic.get())
                d = float(d_cubic.get())
                x1, x2, x3 = self.engine.solve_cubic(a, b, c, d)
                result_cubic.delete(1.0, tk.END)
                result_cubic.insert(tk.END, f"Solutions:\n")
                for i, x in enumerate([x1, x2, x3], 1):
                    if isinstance(x, complex) and x.imag != 0:
                        result_cubic.insert(tk.END, f"x₃ = {x.real:.10g} + {x.imag:.10g}i\n".replace('₃', str(i)))
                    else:
                        val = x.real if isinstance(x, complex) else x
                        result_cubic.insert(tk.END, f"x₃ = {val:.10g}\n".replace('₃', str(i)))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        ttk.Button(cubic_frame, text="Solve", command=solve_cubic).pack(pady=5)
    
    def open_graph_window(self):
        """Open function graphing window."""
        graph_window = tk.Toplevel(self.root)
        graph_window.title("Function Grapher")
        graph_window.geometry("600x550")
        
        # Input frame
        input_frame = ttk.Frame(graph_window)
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(input_frame, text="Function f(x):").grid(row=0, column=0, padx=5)
        func_entry = ttk.Entry(input_frame, width=30)
        func_entry.grid(row=0, column=1, padx=5)
        func_entry.insert(0, "sin(x)")
        
        ttk.Label(input_frame, text="x min:").grid(row=1, column=0, padx=5)
        xmin_entry = ttk.Entry(input_frame, width=10)
        xmin_entry.grid(row=1, column=1, padx=5, sticky='w')
        xmin_entry.insert(0, "-10")
        
        ttk.Label(input_frame, text="x max:").grid(row=2, column=0, padx=5)
        xmax_entry = ttk.Entry(input_frame, width=10)
        xmax_entry.grid(row=2, column=1, padx=5, sticky='w')
        xmax_entry.insert(0, "10")
        
        # Create matplotlib figure
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)
        
        canvas = FigureCanvasTkAgg(fig, graph_window)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        def plot_function():
            try:
                func_str = func_entry.get()
                xmin = float(xmin_entry.get())
                xmax = float(xmax_entry.get())
                
                x_vals = np.linspace(xmin, xmax, 500)
                y_vals = []
                
                for x in x_vals:
                    try:
                        y = self.engine.evaluate(func_str.replace('x', str(x)))
                        if isinstance(y, complex):
                            y = y.real if abs(y.imag) < 1e-10 else float('nan')
                        y_vals.append(y)
                    except:
                        y_vals.append(float('nan'))
                
                ax.clear()
                ax.plot(x_vals, y_vals, 'b-', linewidth=2)
                ax.grid(True, alpha=0.3)
                ax.axhline(y=0, color='k', linewidth=0.5)
                ax.axvline(x=0, color='k', linewidth=0.5)
                ax.set_xlabel('x')
                ax.set_ylabel('f(x)')
                ax.set_title(f'f(x) = {func_str}')
                canvas.draw()
                
            except Exception as e:
                messagebox.showerror("Plotting Error", str(e))
        
        ttk.Button(input_frame, text="Plot", command=plot_function).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Initial plot
        plot_function()
    
    def open_statistics(self):
        """Open statistics calculator window."""
        stats_window = tk.Toplevel(self.root)
        stats_window.title("Statistics Calculator")
        stats_window.geometry("400x450")
        
        ttk.Label(stats_window, text="Enter data (one value per line):", font=('Arial', 11)).pack(pady=10)
        
        data_text = scrolledtext.ScrolledText(stats_window, height=10, width=40)
        data_text.pack(padx=10, pady=10)
        data_text.insert(tk.END, "1\n2\n3\n4\n5")
        
        result_text = scrolledtext.ScrolledText(stats_window, height=10, width=40)
        result_text.pack(padx=10, pady=10)
        
        def calculate_stats():
            try:
                data_str = data_text.get(1.0, tk.END).strip()
                data = [float(x.strip()) for x in data_str.split('\n') if x.strip()]
                
                stats = self.engine.statistics(data)
                
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, "Statistical Results:\n")
                result_text.insert(tk.END, "=" * 30 + "\n")
                result_text.insert(tk.END, f"Count (n):         {stats['n']}\n")
                result_text.insert(tk.END, f"Sum (Σx):          {stats['sum']:.10g}\n")
                result_text.insert(tk.END, f"Mean (x̄):          {stats['mean']:.10g}\n")
                result_text.insert(tk.END, f"Sum of squares:    {stats['sum_squares']:.10g}\n")
                result_text.insert(tk.END, f"Pop. Std Dev (σ):  {stats['pop_std']:.10g}\n")
                result_text.insert(tk.END, f"Sample Std Dev (s):{stats['sample_std']:.10g}\n")
                result_text.insert(tk.END, f"Minimum:           {stats['min']:.10g}\n")
                result_text.insert(tk.END, f"Maximum:           {stats['max']:.10g}\n")
                
            except Exception as e:
                messagebox.showerror("Statistics Error", str(e))
        
        ttk.Button(stats_window, text="Calculate", command=calculate_stats).pack(pady=5)
    
    def open_base_converter(self):
        """Open base conversion window."""
        conv_window = tk.Toplevel(self.root)
        conv_window.title("Base Converter")
        conv_window.geometry("400x300")
        
        ttk.Label(conv_window, text="Number Base Converter", font=('Arial', 12, 'bold')).pack(pady=10)
        
        input_frame = ttk.Frame(conv_window)
        input_frame.pack(padx=20, pady=10, fill=tk.X)
        
        ttk.Label(input_frame, text="Number:").grid(row=0, column=0, sticky='w', pady=5)
        number_entry = ttk.Entry(input_frame, width=30)
        number_entry.grid(row=0, column=1, pady=5)
        
        ttk.Label(input_frame, text="From Base:").grid(row=1, column=0, sticky='w', pady=5)
        from_base_var = tk.StringVar(value="10")
        from_base = ttk.Combobox(input_frame, textvariable=from_base_var, 
                                  values=["2", "8", "10", "16"], width=10)
        from_base.grid(row=1, column=1, sticky='w', pady=5)
        
        ttk.Label(input_frame, text="To Base:").grid(row=2, column=0, sticky='w', pady=5)
        to_base_var = tk.StringVar(value="2")
        to_base = ttk.Combobox(input_frame, textvariable=to_base_var,
                               values=["2", "8", "10", "16"], width=10)
        to_base.grid(row=2, column=1, sticky='w', pady=5)
        
        result_label = ttk.Label(conv_window, text="Result: ", font=('Arial', 11))
        result_label.pack(pady=20)
        
        def convert():
            try:
                number = number_entry.get().strip()
                from_b = int(from_base_var.get())
                to_b = int(to_base_var.get())
                
                result = self.engine.convert_base(number, from_b, to_b)
                result_label.config(text=f"Result: {result}")
                
            except Exception as e:
                messagebox.showerror("Conversion Error", str(e))
        
        ttk.Button(conv_window, text="Convert", command=convert).pack(pady=10)
    
    def show_about(self):
        """Show about dialog."""
        about_text = """Casio FX-991 CN X Calculator
        
Version: 1.0
Cross-platform scientific calculator

Features:
• Basic and scientific calculations
• Equation solver (linear, quadratic, cubic)
• Function graphing
• Statistics calculations
• Base conversion
• Multiple angle modes

© 2024 - Educational Project"""
        
        messagebox.showinfo("About", about_text)
    
    def show_help(self):
        """Show help dialog."""
        help_window = tk.Toplevel(self.root)
        help_window.title("Help")
        help_window.geometry("500x400")
        
        help_text = scrolledtext.ScrolledText(help_window, wrap=tk.WORD, width=60, height=20)
        help_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        help_content = """CASIO FX-991 CN X CALCULATOR - HELP

BASIC OPERATIONS:
• Use number buttons and operation buttons for calculations
• Press '=' to calculate result
• Use 'clear' to clear display, 'del' to delete last character

FUNCTIONS:
• sin, cos, tan: Trigonometric functions (respects angle mode)
• sin⁻¹, cos⁻¹, tan⁻¹: Inverse trigonometric functions
• x²: Square, √: Square root, ^: Power
• log: Base-10 logarithm, ln: Natural logarithm
• x!: Factorial, abs: Absolute value
• π: Pi constant, e: Euler's number
• Ans: Last answer

ANGLE MODES:
• Deg: Degrees (default)
• Rad: Radians
• Grad: Gradians
Change via Mode menu or mode button

EQUATION SOLVER:
Tools → Equation Solver
• Linear: ax + b = 0
• Quadratic: ax² + bx + c = 0
• Cubic: ax³ + bx² + cx + d = 0

FUNCTION GRAPHER:
Tools → Function Grapher
• Enter function in terms of x
• Set x range (min and max)
• Click Plot to graph

STATISTICS:
Tools → Statistics
• Enter data values (one per line)
• Calculate mean, std dev, min, max, etc.

BASE CONVERTER:
Tools → Base Converter
• Convert between binary, octal, decimal, hexadecimal
• Supports bases: 2, 8, 10, 16

EXAMPLES:
• sin(45) - sine of 45° (in degree mode)
• sqrt(16) - square root of 16
• 2**3 - 2 raised to power 3
• factorial(5) - factorial of 5
• log(100) - log base 10 of 100
"""
        
        help_text.insert(tk.END, help_content)
        help_text.config(state=tk.DISABLED)
        
        ttk.Button(help_window, text="Close", command=help_window.destroy).pack(pady=5)


def main():
    """Main function to run the GUI calculator."""
    root = tk.Tk()
    app = CasioCalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
