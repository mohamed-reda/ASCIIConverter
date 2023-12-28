from aqdefreader import DfqFile, create_column_dataframe
import aqdefreader as aqdef_reader
from aqdefreader import read_dfq_file
from aqdefreader import DfqFile

# file = "sample_data.txt"
# file = "sample_data.dfq"
file = "sample_data.asc"

# with open(file, "r") as f:
#     lines = f.read()
#     lines = lines.splitlines()
#     df = DfqFile(lines)
#     print(lines)

import aqdefreader

aqdef_data = aqdefreader.read_dfq_file(file)

print("Parts:")
for part in aqdef_data.parts:
    print("- Part Number:", part.part_number)
print("Characteristics:")
for characteristic in create_column_dataframe(aqdef_data.parts):
    print("- Name:", characteristic.name)
    print("  Unit:", characteristic.unit)
    print("  Nominal:", characteristic.nominal)
    print("  Tolerance:", characteristic.tolerance)
