# 1
SELECT countries.name, languages.language, languages.percentage FROM countries
	JOIN languages ON countries.id = languages.country_id
	WHERE languages.language = 'Slovene'
    ORDER BY languages.percentage DESC;

# 2
SELECT countries.name, COUNT(cities.id) AS num_cities FROM cities
	JOIN countries ON cities.country_id = countries.id
    GROUP BY countries.id
    ORDER BY num_cities DESC;

# 3
SELECT cities.name, cities.population FROM cities
	JOIN countries ON countries.id = cities.country_id
    WHERE cities.population > 500000
    AND countries.name = 'Mexico'
    ORDER BY cities.population DESC;

# 4
SELECT countries.name, languages.language, languages.percentage FROM languages
	INNER JOIN countries ON languages.country_id = countries.id
    WHERE languages.percentage > 89
    ORDER BY languages.percentage DESC, countries.name ASC;

#5
SELECT name, surface_area, population FROM countries
	WHERE surface_area < 501
    AND population > 100000
    ORDER BY population / surface_area DESC;

#6
SELECT name, capital, life_expectancy FROM countries
	WHERE government_form = 'Constitutional Monarchy'
    AND capital > 200
	AND life_expectancy > 75;

#7
SELECT countries.name, cities.name, cities.district, cities.population FROM countries
	JOIN cities ON countries.id = cities.country_id
    WHERE countries.name = 'Argentina'
    AND cities.district = 'Buenos Aires'
    AND cities.population > 500000
    ORDER BY cities.population DESC;

#8
SELECT countries.region, COUNT(*) AS num_countries FROM countries
	GROUP BY countries.region
    ORDER BY num_countries DESC;
