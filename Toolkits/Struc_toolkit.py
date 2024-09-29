# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Structural Material Optimization Tool

class StructuralMaterialOptimizationTool:
    def __init__(self):
        print("Welcome to Structural Material Optimization Toolkit!")
    
    # Function to input material properties
    def input_material_properties(self):
        print("Enter material properties:")
        self.material_density = float(input("Enter the material density (kg/m^3): "))
        self.yield_strength = float(input("Enter the yield strength of the material (MPa): "))
        self.youngs_modulus = float(input("Enter the Young's Modulus (GPa): "))
        self.unit_cost = float(input("Enter the unit cost of material (per kg): "))
        print(f"\nMaterial Properties: Density = {self.material_density} kg/m^3, Yield Strength = {self.yield_strength} MPa, Young's Modulus = {self.youngs_modulus} GPa, Unit Cost = {self.unit_cost}/kg")

    # Function to input load details
    def input_loads(self):
        print("\nEnter load details:")
        self.dead_load = float(input("Enter the dead load (kN): "))
        self.live_load = float(input("Enter the live load (kN): "))
        self.wind_load = float(input("Enter the wind load (kN): "))
        self.total_load = self.dead_load + self.live_load + self.wind_load
        print(f"\nTotal Load = {self.total_load} kN")
    
    # Function to optimize beams
    def optimize_beam(self):
        print("\n--- Beam Optimization ---")
        self.beam_length = float(input("Enter the beam length (m): "))
        self.beam_width = float(input("Enter the initial beam width (mm): "))
        self.beam_height = float(input("Enter the initial beam height (mm): "))
        
        # Calculate moment (M = w * L^2 / 8 for uniform load)
        self.moment = (self.total_load * self.beam_length**2) / 8
        
        # Calculate required section modulus (S = M / sigma)
        self.section_modulus = (self.moment * 1e6) / self.yield_strength  # in mm^3
        
        # Calculate optimized height (S = (b*h^2) / 6)
        self.optimized_beam_height = np.sqrt((6 * self.section_modulus) / self.beam_width)
        
        # Optimized cross-sectional area and volume
        self.optimized_area_beam = self.beam_width * self.optimized_beam_height
        self.optimized_volume_beam = self.optimized_area_beam * self.beam_length * 1e-6  # in m^3
        
        # Material weight and cost
        self.beam_weight = self.optimized_volume_beam * self.material_density  # in kg
        self.beam_cost = self.beam_weight * self.unit_cost  # in currency

        print(f"Optimized Beam Height = {self.optimized_beam_height:.2f} mm")
        print(f"Beam Weight = {self.beam_weight:.2f} kg, Cost = {self.beam_cost:.2f} currency units")

    # Function to optimize columns
    def optimize_column(self):
        print("\n--- Column Optimization ---")
        self.column_length = float(input("Enter the column length (m): "))
        self.column_width = float(input("Enter the initial column width (mm): "))
        self.column_height = float(input("Enter the initial column height (mm): "))
        
        # Calculate axial load capacity (P = σ * A)
        self.axial_capacity = (self.yield_strength * self.column_width * self.column_height * 1e-6)  # in kN

        # Optimize column dimensions (reduce size to match load requirements)
        self.optimized_area_column = self.total_load / self.yield_strength
        self.optimized_column_width = np.sqrt(self.optimized_area_column * 1e6)
        
        # Optimized column volume
        self.optimized_volume_column = self.optimized_column_width**2 * self.column_length * 1e-6  # in m^3
        
        # Material weight and cost
        self.column_weight = self.optimized_volume_column * self.material_density  # in kg
        self.column_cost = self.column_weight * self.unit_cost  # in currency
        
        print(f"Optimized Column Width = {self.optimized_column_width:.2f} mm")
        print(f"Column Weight = {self.column_weight:.2f} kg, Cost = {self.column_cost:.2f} currency units")

    # Function to optimize slabs
    def optimize_slab(self):
        print("\n--- Slab Optimization ---")
        self.slab_thickness = float(input("Enter the initial slab thickness (mm): "))
        self.slab_area = float(input("Enter the slab area (m^2): "))
        
        # Calculate the optimized slab thickness (assuming uniform load distribution)
        self.optimized_slab_thickness = self.total_load / (self.yield_strength * self.slab_area * 1e-6)
        
        # Optimized slab volume
        self.optimized_volume_slab = self.optimized_slab_thickness * self.slab_area * 1e-3  # in m^3
        
        # Material weight and cost
        self.slab_weight = self.optimized_volume_slab * self.material_density  # in kg
        self.slab_cost = self.slab_weight * self.unit_cost  # in currency
        
        print(f"Optimized Slab Thickness = {self.optimized_slab_thickness:.2f} mm")
        print(f"Slab Weight = {self.slab_weight:.2f} kg, Cost = {self.slab_cost:.2f} currency units")
    
    # Function to generate trade-off analysis
    def tradeoff_analysis(self):
        print("\n--- Trade-Off Analysis ---")
        material_usage = np.array([self.beam_weight, self.column_weight, self.slab_weight])
        costs = np.array([self.beam_cost, self.column_cost, self.slab_cost])
        
        plt.figure(figsize=(8, 6))
        plt.bar(["Beam", "Column", "Slab"], material_usage, color=['b', 'g', 'r'])
        plt.title("Material Usage Comparison")
        plt.ylabel("Material Weight (kg)")
        plt.show()
        
        plt.figure(figsize=(8, 6))
        plt.bar(["Beam", "Column", "Slab"], costs, color=['b', 'g', 'r'])
        plt.title("Cost Comparison")
        plt.ylabel("Cost (Currency)")
        plt.show()

    # Function to generate report
    def generate_report(self):
        print("\n--- Optimization Report ---")
        report = {
            "Material Density (kg/m^3)": self.material_density,
            "Yield Strength (MPa)": self.yield_strength,
            "Young's Modulus (GPa)": self.youngs_modulus,
            "Unit Cost (/kg)": self.unit_cost,
            "Total Load (kN)": self.total_load,
            "Optimized Beam Height (mm)": self.optimized_beam_height,
            "Optimized Column Width (mm)": self.optimized_column_width,
            "Optimized Slab Thickness (mm)": self.optimized_slab_thickness,
            "Beam Weight (kg)": self.beam_weight,
            "Column Weight (kg)": self.column_weight,
            "Slab Weight (kg)": self.slab_weight,
            "Beam Cost (Currency)": self.beam_cost,
            "Column Cost (Currency)": self.column_cost,
            "Slab Cost (Currency)": self.slab_cost
        }
        
        report_df = pd.DataFrame(list(report.items()), columns=["Parameter", "Value"])
        print(report_df)

# Main function to run the tool
def main():
    tool = StructuralMaterialOptimizationTool()
    
    # Input material properties and load details
    tool.input_material_properties()
    tool.input_loads()
    
    # Optimize structure components
    tool.optimize_beam()
    tool.optimize_column()
    tool.optimize_slab()
    
    # Provide trade-off analysis
    tool.tradeoff_analysis()
    
    # Generate optimization report
    tool.generate_report()

# Run the tool
if __name__ == "__main__":
    main()
