import DataReader as dataReader
import Player as player

if __name__ == "__main__":
    reader = dataReader.DataReader()
    reader.prepare_data()

    data = reader.get_data()

    player = player.Player()

    for city in data["Name"]:
        player.guess(city)

    input("Press enter to exit...")