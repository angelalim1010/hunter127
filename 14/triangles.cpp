#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;
std::string line(int l, std::string c){
  string s = "";
  for (int i=0; i<l;i++){
    s+=c;
  }
  
  return s;




  return "";
}

std::string rect(int w, int h) {
  string s = "";
  for (int i=0; i<h; i++){
    s+=line(w,"*")+"\n";
  }return s;

  return "";
}

/*
 *
 **
 ***
 ****
 */
std::string tri1(int h) {
  string s = "";
  for (int i=0; i<h; i++){
    s+=line(i+1,"*")+"\n";
  }return s;


  return "";
}


/*
   *
  ***
 *****
 */
std::string tri2(int h) {
  
  string s="";
  for(int i=0; i<h; i++){
    int space = (2*h-2*i-1)/2;
    s+=std::string(space,' ')+line(2*i+1,"*")+std::string(space,' ')+'\n';
  }
  return s;

  return "";
}

/*
  *
 **
***
 */
std::string tri3(int h) {
  string s ="";
  for(int i=0; i<h; i++){
    s+=std::string(h-i-1,' ')+ line(i+1,"*")+"\n";
  }
  return s;

  return "";
}
int main(){
  string s="hello";
  cout << line(1, "*") << endl;
  cout << rect(4,5) << endl;
  cout << tri1(4) << endl;
  cout << tri2(3) << endl;
  cout << tri3(3) << endl;
  cout<<s<<endl;
}

