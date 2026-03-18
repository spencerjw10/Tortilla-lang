#include "lexer.h"
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class token {
public:
    string kind; //Kinds: Variable Name, Keyword, Operator, Int, Float, Bool, Str
    string val; //Value or specific type e.g. king = Operator, val = 'Plus'
    int line; //Line number
    int col; //Column
    token(string k, string v, int l, int c) {
        kind = k;
        val = v;
        line = l;
        col = c;
    }
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
string getDoubOp(char first, char second) {
    switch(first) {
        case '+':
            switch(second) {
            case '+': return "Inc";
            case '=': return "PlusEql";
            default:  return "";
            }
        case '-':
            switch(second) {
            case '-': return "Dec";
            case '=': return "MinusEql";
            default:  return "";
            }
        case '*':
            switch(second) {
            case '*': return "Power";
            case '=': return "TimesEql";
            default:  return "";
            }
        case '/':
            switch(second) {
            case '=': return "DivideEql";
            default:  return "";
            }
        case '%':
            switch(second) {
            case '=': return "ModEql";
            default:  return "";
            }
        case '<':
            switch(second) {
            case '=': return "Lte";
            case '<': return "Shl";
            default:  return "";
            }
        case '>':
            switch(second) {
            case '=': return "Gte";
            case '>': return "Shr";
            default:  return "";
            }
        default: return "";
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
    string value = " ";
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
        //Increment line and column
        if (code[i] == '\n') {
            line += 1;
            col = 0;
        }
        else {
            col += 1;
        }

        //Comment Removal
        if (mode == 1 or mode == 2) {
            if (i + 1 < code.length() and code[i] == '#' and code[i + 1] == '#') {
                i += 1;
                mode = 0;
            }
            else if (mode == 1 and code[i] == '\n') {
                mode = 0;
                i += 1;
            }
        }
        //String Mode
        else if (mode == 3) {
            //Repeats until it finds the correct end quote
            if (code[i] == qot) {
                token curTok = token("Str", value, line, col);
                tokens.push_back(curTok);
                value = " ";
                mode = 0;
            }
            else {
                value += code[i];
            }
            i += 1;
        }
        mode += 1;
    }
    return 0;
}
