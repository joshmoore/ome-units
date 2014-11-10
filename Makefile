# exclude Angle
units ?= units/UnitsElectricPotential.txt units/UnitsFrequency.txt units/UnitsLength.txt units/UnitsPressure.txt units/UnitsPower.txt units/UnitsTemperature.txt units/UnitsTime.txt
files: $(units)

model: model/UnitsElectricPotential.java model/UnitsFrequency.java model/UnitsLength.java model/UnitsPressure.java model/UnitsPower.java model/UnitsTemperature.java model/UnitsTime.java
sql: sql/UnitsElectricPotential.sql sql/UnitsFrequency.sql sql/UnitsLength.sql sql/UnitsPressure.sql sql/UnitsPower.sql sql/UnitsTemperature.sql sql/UnitsTime.sql

blitz: files
	./gen.py --combine templates/blitz $(units) > $@

model/%.java: units/%.txt
	mkdir -p model
	./gen.py templates/model $< > $@

sql/%.sql: units/%.txt
	mkdir -p sql
	./gen.py templates/sql $< > $@

clean:
	rm -rf blitz model sql

.PHONY: sql files model clean
