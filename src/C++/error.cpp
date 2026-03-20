#include "error.h"
#include <vector>
#include <string>
#include <utility>
using namespace std;

Error::Error(string k, string m, int n, int l, int c) {
    kind = std::move(k);
    message = std::move(m);
    numb = n;
    line = l;
    col = c;
};

vector<Error> errs;

void readErrors(std::vector<Error> errors){};
/* vals vector takes different things for each error type:
Error 1: [letter that caused error]
Error 2: []
 */
void addError(string kind, int numb, int line, int col, vector<string> vals) {
    string message = "Error " + to_string(numb) + ": ";
    string message2;
    switch (numb) {
        case(1):
            message += "Syntax Error ";
            message2 = "Unexpected character " + vals[0];
        case(2):
            message += "Syntax Error ";
            message2 = "No " + vals[0];
        default:
            message += "Unkown Error";
    }
    message += "at line " + to_string(line) + ", column " + to_string(col) + ".";
    /*
    Incorrect Syntax: hard error
    Empty code block/statement: hard error
    Call nonexistent thing: error
    Hard error at compile time
    Soft error at runtime
    Divide by 0: soft error, return null
    Overflow error: soft error, return null
    Use null in an operation: soft error, null = 0
    Variable turns into null: soft error, points to error 8 if logical
    Assign func/class w/o return: return null
    Initlize wrong DT: soft error, change DT
    Assign wrong DT: soft error, ignore change //Also points to error 9 if DT was changed
 */
    Error newErr = Error(kind, message, numb, line, col);
    errs.push_back(newErr);

};
bool hasHard(std::vector<Error> errors) {
    return false;
};