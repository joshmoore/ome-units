all: clean blitz/Units.ice blitz2 model sql

# exclude Angle
units ?= units/ElectricPotential.txt units/Frequency.txt  units/Length.txt  units/Pressure.txt  units/Power.txt  units/Temperature.txt  units/Time.txt
files: $(units)

model:  model/UnitsElectricPotential.java model/UnitsFrequency.java model/UnitsLength.java model/UnitsPressure.java model/UnitsPower.java model/UnitsTemperature.java model/UnitsTime.java
sql:    sql/UnitsElectricPotential.sql    sql/UnitsFrequency.sql    sql/UnitsLength.sql    sql/UnitsPressure.sql    sql/UnitsPower.sql    sql/UnitsTemperature.sql    sql/UnitsTime.sql
blitz2: blitz/ElectricPotential.ice       blitz/Frequency.ice       blitz/Length.ice       blitz/Pressure.ice       blitz/Power.ice       blitz/Temperature.ice       blitz/Time.ice

blitz/Units.ice: files
	mkdir -p blitz
	./gen.py --combine templates/Units.ice $(units) > $@

blitz/%.ice: units/%.txt
	mkdir -p blitz
	./gen.py templates/blitz.ice $< > $@

model/Units%.java: units/%.txt
	mkdir -p model
	./gen.py templates/model $< > $@

sql/Units%.sql: units/%.txt
	mkdir -p sql
	./gen.py templates/sql $< > $@

clean:
	rm -rf blitz model sql

.PHONY: sql files model clean
