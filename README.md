# Spiref: Spirometry Reference Value Calculator
This package contains the reference value calculator for spirometry. Can be installed immediately using pip:
````
pip install spiref
````

Currently supported:
* NHANES III
* GLI-2012 (https://www.ers-education.org/lrMedia/2013/pdf/266709.pdf)

Parameters:

  * sex: either 'male' or 'female'.
  * height: the height of the person in centimeter.
  * age: the age in years.
  * race: different options for NHANES III and GLI-2012 (see below).

### NHANES III 
Race options for NHANES III:  'Cau', 'AfrAm', 'MexAm' (Causasian, African-American or Mexican-American).

### GLI-2012
Either the general calculation function (calc_lung_param) or the specific calculation functions (analogue to the NHANES calculator) can be used.
Use the function calc_lln_lung_param with the same parameters as calc_lung_param to compute the lower limit of normal (LNN or 5th percentile).

Possible lung parameters are: 'FEV1', 'FVC', 'FEV1FVC', 'FEF2575', 'FEF75'.

Race options for GLI-2012: 'Cau', 'AfrAm', 'NEAsia', 'SEAsia', 'other' (Caucasian, African-American, North-East Asia, South-East Asia, other).


## Usage
For NHANES III:
```python
from spiref import nhanes3

# Load the calculator
rvc = nhanes3.NHANESReferenceValueCalculator()

# Use the calculator to compute FEV1 for a male of height 174cm, age 28 of the African-American race.
fev1 = rvc.calculate_fev1('male', 174, 28, race='AfrAm')
```

For GLI12:
```python
from spiref import gli12

# Load the calculator
rvc = gli12.GLIReferenceValueCalculator()

# The general calculator function:
fev1 = rvc.cal_lung_param('FEV1', 'male', 174, 28, 'AfrAm')  # African-American male, height 174 cm, age 28
# Same can be achieved with the specific FEV1 function:
fev1 = rvc.calculate_fev1('male', 174, 28, race='AfrAm')

# Computing the lower limit of normal (5th percentile)
fev1_lln = rvc.calc_lln_lung_param('FEV1', 'male', 174, 28, 'AfrAm')

```
