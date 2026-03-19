#include "lexer.h"
#include <string>
#include <unordered_set>
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
    string value = "";
    string abc = "asdfghjklqwertyuiopzxcvbnmASDFGHJKLQWERTYUIOPZXCVBNM_";
    string blank = " \n\t";
    string nums = "1234567890";
    unordered_set<string> keywords = {
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
        //Normal Mode
        else if (mode == 0) {
            if (blank.find(code[i]) != string::npos) {
                i += 1;
            }
            else if (code[i] == '#') {
                i += 1;
                if (code[i] == '#') {
                    mode = 2;
                    i += 1;
                }
                else {
                    mode = 1;
                }
            }
            //Checks for Number Literals
            else if (nums.find(code[i]) != string::npos) {
                //If point becomes True, number is a float
                bool point = false;
                string num;
                num = code[i];
                i += 1;
                while (nums.find(code[i]) != string::npos or code[i] == '.') {
                    num += code[i];
                    if (code[i] == '.'){
                        if (point == true){
                        }
                        point = true;
                    }
                    i += 1;
                }
                if (point) {
                    token curTok = token("Float", num, line, col);
                    tokens.push_back(curTok);
                }
                else {
                    token curTok = token("Int", num, line, col);
                    tokens.push_back(curTok);
                }
            }
            //Starts a String
            else if (code[i] == '`' or code[i] == '`' or code[i] == '\"') {
                mode = 3;
                //Type of quote to look for
                qot = code[i];
                i += 1;
            }
            else if (getDoubOp(code[i], code[i + 1]) != "") {
                token curTok = token("Operator", getDoubOp(code[i], code[i + 1]), line, col);
                tokens.push_back(curTok);
                i += 2;
            }
            else if (getSingOp(code[i]) != "") {
                token curTok = token("Operator", getSingOp(code[i]), line, col);
                tokens.push_back(curTok);
                i += 1;
            }
            else if (abc.find(code[i]) != string::npos) {
                string word;
                word = code[i];
                i += 1;
                //Adds characters to the word until it finds a non number, letter, or underspace
                while (abc.find(code[i]) != string::npos or nums.find(code[i]) != string::npos) {
                    word += code[i];
                    i += 1;
                }
                if (word == "true" or word == "false") {
                    token curTok = token("Bool", word, line, col);
                    tokens.push_back(curTok);
                }
                else if (keywords.count(word)) {
                    token curTok = token("Keyword", word, line, col);
                    tokens.push_back(curTok);
                }
                else {
                    token curTok = token("Variable", word, line, col);
                    tokens.push_back(curTok);
                }
            }
        }
        //String Mode
        else {
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
    }
    return 0;
}