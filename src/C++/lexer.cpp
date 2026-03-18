#include "lexer.h"
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class token {
    public:
        string kind; //Kinds: Variable Name, Keyword, Operator, Int, Float, Bool, Str
        string val; //Value or specific type e.g. king = Operator, val = 'Plus'
        int line;  //Line number
        int col; //Column
};
string getSingOp(char c) {
    switch(c) {
        case '+': return "Plus";
        case '*': return "Times";
        case '-': return "Minus";
        case '/': return "Divide";
        case '=': return "Assign";
        case '%': return "Mod";
        case '!': return "BitNot";
        case '&': return "BitAnd";
        case '^': return "BitXor";
        case '|': return "BitOr";
        case '(': return "Lpar";
        case ')': return "Rpar";
        case '[': return "Lbrc";
        case ']': return "Rbrc";
        case '<': return "Less";
        case '>': return "More";
        case '{': return "Lbrkt";
        case '}': return "Rbrkt";
        case ':': return "Then";
        case '.': return "Point";
        case ';': return "Semi";
        case ',': return "Comma";
        default:  return "";   // not a single operator
    }
}


string code = "";
int main() {
    int i = 0;
    vector<token> tokens;
    code += " ";  //Adds an ending space to the code so that the index does not go out of bounds
    int mode = 0; //0 = Normal, 1 = Single-line Comment, 2 = Multi-line Comment, 3 = String
    int line = 0;
    int col = 0;
    char qot = ' ';  //Quotation Type for Strings
    auto value = ' ';
    string abc = "asdfghjklqwertyuiopzxcvbnmASDFGHJKLQWERTYUIOPZXCVBNM_";
    string keywords[48] = {
        "is", "not", "in", "has", "xor", "nor", "and",
        "or", "null", "int", "bigInt", "float", "doub",
        "char", "str", "bool", "array", "set", "dict",
        "class", "func", "if", "elif", "else", "switch",
        "case", "default", "for", "while", "forEach",
        "return", "out", "this", "const", "extends",
        "parent", "type", "label", "goto", "await",
        "async", "pfor", "try", "soft", "hard", "catch",
        "also", "end"

    };

    while (i < code.length()) {

    }
    return 0;
}
