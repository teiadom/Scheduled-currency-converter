import csv
import time
import calendar
import exchange_rate_api as exchange_rate


def get_formatted_data(result_set):

    # This takes only needed keys from the result_set dict to format properly
    header_keys = ('time_zone', 'time_last_update', 'time_next_update', 'base')
    exchange_key = 'conversion_rates'
    header_dict = {k: result_set[k] for k in header_keys}
    exchange_dict = result_set.get(exchange_key)
    formatted_data = {**header_dict, **exchange_dict}

    return formatted_data


def write_data_csv(data):

    # This method writes the data to an excel file with the epoch timestamp as the name of the file.
    cur_timestamp = calendar.timegm(time.gmtime())
    data_write = get_formatted_data(data)
    file_name = str(cur_timestamp)+".csv"

    with open(file_name, "w") as csv_output:
        writer = csv.writer(csv_output)
        for i in data_write:
            writer.writerow([i, data_write[i]])
    csv_output.close()


def exchange_rate_usd():
    result = exchange_rate.ExchangeRateAPI('EXCHANGE_RATE_USD').get()

    try:
        write_data_csv(result)
        print("Data saved successfully...")
    except Exception as e:
        print("Excel writer error: " + str(e))


if __name__ == '__main__':
    exchange_rate_usd()