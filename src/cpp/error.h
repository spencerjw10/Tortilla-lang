#ifndef TORTILLA_ERROR_H
#define TORTILLA_ERROR_H
#include <vector>
#include <string>

class Error {
    public:
        std::string kind;  //soft hard
        std::string message;
        int numb;
        int line;
        int col;
        Error(std::string k, std::string m, int n, int l, int c);
};

void readErrors(std::vector<Error> errors);
void addError(std::string kind, int numb, int line, int col);
bool hasHard(std::vector<Error> errors);

#endif