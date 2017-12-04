#include <iostream>
int lone_sums (int a, int b, int c){
	if (a == b == c){
		std::cout << 0;
	} else if (a == b){
		std::cout << c;
	} else if (b == c){
		std::cout << a;
	} else if (a == c){
		std::cout << b;
	} return a + b + c;
}
int cigars_party(int cigars,bool is_weekend){
	if (is_weekend){
			if (cigars >= 40){
			return  true;
		}return false;
		}else{
			if (cigars >= 40 and cigars <= 60){
				return true;
			return false;
			}
		}

	}
int caught_speeding (int speed, bool is_birthday){
	  int gift;
	  gift = 0;
  if (is_birthday){
  	int gift = 5;
  }
    
  if (speed <= 60+gift){
  	return 0;
  }
    
  else if (speed >= 81+gift){
    return 2;
} return 1;
}




int main(){
	int a = 1;
		int b = 2;
		int c = 3;
	int x;
	x = lone_sums(a,b,c);
	std::cout << x << std::endl;

	int cigars = 30;
		 bool is_weekend = false;
		bool z;
		z = cigars_party(cigars, is_weekend);
		std::cout << z << std::endl;

	int speed = 60;
	bool is_birthday = false;
	int y;
	y = caught_speeding(speed, is_birthday);
	std::cout << y << std::endl;

	return 0;
}
 

