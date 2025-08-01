import DataReader as dataReader

if __name__ == "__main__":
    reader = dataReader.DataReader()
    reader.prepare_data()

    print(reader.get_data())