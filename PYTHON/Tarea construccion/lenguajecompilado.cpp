#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


class Producto{
    public:
    string nombre;
    string descripcion;
    float precio;
    Producto(string n, string d, float p){
	this->nombre = n;
	this->descripcion = d;
	this->precio = p;
    }
};

class Util : public Producto{
    private:
	int existencia;
    public:
	Util(string, string, int, float);
	void _print();
	Util();
};

void Util::_print(){
    cout << "Util: " << this->nombre << " -- Descripcion: " << this->descripcion;
    cout << " -- " << " Total en existencia: " << this->existencia << " -- precio: "  << this->precio << endl;
}

Util::Util():Producto("", "", 0){
    this->existencia = 0;
}

Util::Util(string nom, string des, int c, float p):Producto(nom, des, p){
    this->existencia = c;
}




void agregar(vector<Util> &utiles){
    string nom;
    string des;
    int cant; float prec;
    cout << "Nombre del produco: "; cin >> nom;
    cout << "Descripcion: "; cin >> des;
    cout << "Cantidad en existencia: "; cin >> cant;
    cout << "Precio: "; cin >> prec;

    Util nuevo = Util();
    nuevo = Util(nom, des, cant, prec);
    utiles.push_back(nuevo);
    cout << "Producto Guardado Correctamente 😃" << endl;
}


void mostrar(vector<Util>* utiles){
    for(int i =0 ; i < utiles->size(); i++){
	utiles->at(i)._print();
    }
}

int buscar(vector<Util> utiles, string referencia){
    for(int i = 0; i < utiles.size(); i++){
	if(utiles[i].nombre == referencia){
	    return i;
	}
    }
    return -1;
}


void eliminar(vector<Util> &utiles, string referencia){
    int pos = buscar(utiles, referencia);
    if(pos != -1){
	utiles.erase(utiles.begin() + pos);
	cout << "Eliminado correctamente" << endl;
    }
    else{
	cout << "NO se encontro este producto \n";

    }
}

int main(){
    int opcion;
    vector<Util> utiles;

    do{
	system("cls");
	cout << "1- Agregar util \n";
	cout << "2- Mostrar Utiles \n";
	cout << "3- Buscar \n";
	cout << "4- Eliminar \n";
	cout << "5- Salir \n";
	cout << "opcion: ";
	cin >> opcion;

	if(opcion == 1){
	    system("cls");
	    agregar(utiles);
	    system("pause");
	}
	else if(opcion == 2){
	    system("cls");
	    vector<Util>* utls = &utiles;
	    mostrar(utls);
	    system("pause");
	}
	else if(opcion == 3){
	    system("cls");
	    string nom;
	    cout << "Nombre a buscar: ";
	    cin >> nom;
	    if(buscar(utiles, nom) != -1){
		utiles[buscar(utiles, nom)]._print();
	    }
	    else{
		cout << "Este producto no fue encontrado";
	    }
	    system("pause");

	}
	else if(opcion == 4){
	    system("cls");
	    string nom;
	    cout << "Nombre a eliminar: ";
	    cin >> nom;
	    eliminar(utiles,nom);
	    system("pause");
	}




    }while(opcion != 5);
}