import cx_Freeze

excutables = [cx_Freeze.Executable("AvoidTheBlocks.py")]

cx_Freeze.setup(
    name = "Avoid The Block"
    options = {"build_exe": {"packages":["pygame"],"included_files": ["car.png"]}},
    excutables = excutables
)
