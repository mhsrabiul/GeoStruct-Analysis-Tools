# GeoStruct-Analysis-Tools

**GeoStruct-Analysis-Tools** is a Python-based toolkit designed for civil and geotechnical engineers. It includes two main tools: 
1. **Soil Classification and Analysis Tool** 
2. **Structural Material Optimization Tool**

These tools help automate soil classification based on various geotechnical properties and optimize material usage in structural designs, ensuring cost-efficiency and safety.

---

## Features

### 1. Soil Classification and Analysis Tool
- **Input**: Grain size distribution (sieve analysis or hydrometer test), Atterberg limits, and moisture content.
- **Output**: Soil classification according to the Unified Soil Classification System (USCS) and graphical representation of grain size distribution curves.
- **Use Case**: Helps classify soil into categories such as gravel, sand, silt, and clay.

### 2. Structural Material Optimization Tool
- **Input**: Material properties (e.g., steel or concrete), loads, and initial structural dimensions.
- **Output**: Optimized beam, column, and slab dimensions to minimize material usage while maintaining structural safety. Includes trade-off analysis between cost, safety, and material usage.
- **Use Case**: Helps engineers minimize material usage while adhering to safety standards.

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/mhsrabiul/GeoStruct-Analysis-Tools.git
    ```
2. Navigate to the project directory:
    ```bash
    cd GeoStruct-Analysis-Tools
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

### Soil Classification and Analysis Tool
1. Run the script:
    ```bash
    python Geo_toolkit.py
    ```
2. Input your grain size distribution, Atterberg limits, and moisture content as prompted.
3. View the soil classification and the generated grain size distribution curve.

### Structural Material Optimization Tool
1. Run the script:
    ```bash
    python Struc_toolkit.py
    ```
2. Input material properties, loads, and initial structural dimensions.
3. Review the optimized dimensions and the trade-off analysis between cost and material usage.

---

## Example Inputs

### Soil Classification and Analysis Tool:
- **Sieve Sizes (mm)**: `4.75, 2.00, 0.425, 0.075`
- **Percent Passing (%):** `100, 70, 45, 8`
- **Liquid Limit (LL):** `40`
- **Plastic Limit (PL):** `20`
- **Moisture Content (%):** `15.2`

### Structural Material Optimization Tool:
- **Material Density (kg/m³):** `7850`
- **Yield Strength (MPa):** `250`
- **Dead Load (kN):** `50`
- **Beam Length (m):** `6`
- **Initial Beam Width (mm):** `300`
- **Initial Column Width (mm):** `400`

---

## Outputs

### Soil Classification Tool:
- Soil classification based on USCS
- Grain size distribution curve
- Atterberg limits analysis

### Material Optimization Tool:
- Optimized dimensions for beams, columns, and slabs
- Cost and material usage analysis
- Trade-off comparison between material usage and safety

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push the branch (`git push origin feature-name`).
5. Create a new pull request.

---

## Contact

For any inquiries, please contact the repository owner at- rabiul1812019@gmail.com

