#include <iostream>
#include <string>
#include "lexer.h"

int main() {
    std::string code = "int a + b";
    std::vector<token> tokens = tokenize(code);
    for (auto & token : tokens) {
        std::cout << token.kind + " " + token.val + "\n";
    }
    return 0;
}
