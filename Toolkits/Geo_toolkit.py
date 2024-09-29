# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.interpolate import interp1d

# Soil Classification and Analysis Tool

class SoilClassificationTool:
    def __init__(self):
        print("Soil Classification and Analysis Toolkit!")
    
    # Function to input sieve analysis data
    def input_sieve_analysis(self):
        print("Enter sieve analysis data:")
        self.sieve_sizes = np.array([75, 19, 4.75, 2, 0.425, 0.075])  # Sieve sizes in mm (75 mm, 19 mm, etc.)
        retained_percentages = []
        for sieve in self.sieve_sizes:
            retained = float(input(f"Enter the percentage retained on {sieve} mm sieve: "))
            retained_percentages.append(retained)
        self.retained_percentages = np.array(retained_percentages)
        self.calculate_cumulative_percent()

    # Calculate cumulative percentage passing
    def calculate_cumulative_percent(self):
        self.passing_percentages = 100 - np.cumsum(self.retained_percentages)
        print("Cumulative passing percentages (in %):", self.passing_percentages)
        self.plot_grain_size_distribution()

    # Function to input Atterberg limits
    def input_atterberg_limits(self):
        print("Enter Atterberg limits data:")
        self.liquid_limit = float(input("Enter the Liquid Limit (LL) in %: "))
        self.plastic_limit = float(input("Enter the Plastic Limit (PL) in %: "))
        self.calculate_plasticity_index()

    # Calculate Plasticity Index (PI)
    def calculate_plasticity_index(self):
        self.plasticity_index = self.liquid_limit - self.plastic_limit
        print(f"Plasticity Index (PI) = {self.plasticity_index} %")
    
    # Classify soil based on grain size distribution and Atterberg limits
    def classify_soil(self):
        if self.passing_percentages[4] < 50:
            if self.passing_percentages[2] > 50:
                if self.plasticity_index < 7:
                    self.soil_class = "Silty Gravel (GM)"
                else:
                    self.soil_class = "Clayey Gravel (GC)"
            else:
                self.soil_class = "Gravel (G)"
        elif self.passing_percentages[5] < 50:
            if self.passing_percentages[4] > 50:
                if self.plasticity_index < 7:
                    self.soil_class = "Silty Sand (SM)"
                else:
                    self.soil_class = "Clayey Sand (SC)"
            else:
                self.soil_class = "Sand (S)"
        else:
            if self.plasticity_index < 4:
                self.soil_class = "Silt (ML)"
            elif self.plasticity_index > 7:
                self.soil_class = "Clay (CL)"
            else:
                self.soil_class = "Silty Clay (CL-ML)"
        print(f"Soil classified as: {self.soil_class}")
    
    # Plot grain size distribution curve
    def plot_grain_size_distribution(self):
        plt.figure(figsize=(8, 6))
        plt.semilogx(self.sieve_sizes, self.passing_percentages, marker='o', linestyle='-', color='b')
        plt.gca().invert_xaxis()  # Reverse x-axis for sieve size
        plt.title("Grain Size Distribution Curve")
        plt.xlabel("Sieve Size (mm)")
        plt.ylabel("Cumulative Passing (%)")
        plt.grid(True)
        plt.show()

    # Input for moisture content
    def input_moisture_content(self):
        print("Enter moisture content data:")
        self.moisture_content = float(input("Enter the moisture content in %: "))
        print(f"Moisture content = {self.moisture_content} %")
    
    # Function to summarize the results
    def display_summary(self):
        print("\n--- Soil Classification Summary ---")
        print(f"Grain Size Distribution: {self.passing_percentages}")
        print(f"Liquid Limit (LL): {self.liquid_limit}%")
        print(f"Plastic Limit (PL): {self.plastic_limit}%")
        print(f"Plasticity Index (PI): {self.plasticity_index}%")
        print(f"Moisture Content: {self.moisture_content}%")
        print(f"Soil Class (USCS): {self.soil_class}")
        print("------------------------------------")

# Main function to run the tool
def main():
    soil_tool = SoilClassificationTool()
    
    # Input the required soil data
    soil_tool.input_sieve_analysis()  # Sieve analysis for grain size
    soil_tool.input_atterberg_limits()  # Atterberg limits (LL and PL)
    soil_tool.input_moisture_content()  # Moisture content
    
    # Classify the soil based on the inputs
    soil_tool.classify_soil()
    
    # Display summary of the analysis
    soil_tool.display_summary()

# Run the tool
if __name__ == "__main__":
    main()
