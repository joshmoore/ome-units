files: Angle.txt ElectricPotential.txt Frequency.txt Length.txt Pressure.txt Power.txt Temperature.txt Time.txt
model: model/Angle.java model/ElectricPotential.java model/Frequency.java model/Length.java model/Pressure.java model/Power.java model/Temperature.java model/Time.java
sql: sql/Angle.sql sql/ElectricPotential.sql sql/Frequency.sql sql/Length.sql sql/Pressure.sql sql/Power.sql sql/Temperature.sql sql/Time.sql

model/%.java: units/%.txt
	mkdir -p model
	./gen.py $< templates/model > $@

sql/%.sql: units/%.txt
	mkdir -p sql
	./gen.py $< templates/sql > $@

clean:
	rm -rf model/* sql/*

.PHONY: sql files model clean
