#ifndef TORTILLA_LANG_LEXER_H
#define TORTILLA_LANG_LEXER_H
#include <string>
#include <vector>

std::string getSingOp(char c);
std::string getDoubOp(char first, char second);

class token {
public:
    std::string kind; //Kinds: Variable Name, Keyword, Operator, Int, Float, Bool, Str
    std::string val; //Value or specific type e.g. king = Operator, val = 'Plus'
    int line; //Line number
    int col; //Column
    token(std::string k, std::string v, int l, int c);
};

std::vector<token> tokenize(std::string code);

#endif