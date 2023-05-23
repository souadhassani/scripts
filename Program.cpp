#include <iostream>
#include <vector>

class DataManager {
private:
    std::vector<int> data;

public:
    void addData(int value) {
        data.push_back(value);
    }

    void printData() {
        for (const auto& value : data) {
            std::cout << value << " ";
        }
        std::cout << std::endl;
    }
};

int main() {
    DataManager manager;

    // Ajouter des données
    manager.addData(10);
    manager.addData(20);
    manager.addData(30);

    // Afficher les données
    manager.printData();

    return 0;
}
