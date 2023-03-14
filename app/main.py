import utils
import read_csv
import charts


def run():
  data = read_csv.read_csv('./app/data.csv')
  data = list(filter(lambda x: x['Continent'] == 'South America', data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentage = list(map(lambda x: x['World Population Percentage'], data))

  charts.generate_pie_chart(countries, percentage)
  country = input('Type Country => ')
  result = utils.population_by_country(data, country)
  if len(result) > 0:
    labels, values = utils.get_population(result[0])
    # charts.generate_pie_chart(labels, values)
    charts.generate_bar_chart(country, labels, values)
  else:
    print('not data')


if __name__ == '__main__':
  run()
