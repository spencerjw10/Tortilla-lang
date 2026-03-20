cmake_minimum_required(VERSION 3.20)
project(Tortilla)

set(CMAKE_CXX_STANDARD 17)

add_executable(Tortilla
        main.cpp
        lexer.cpp
        lexer.h
        error.cpp
        error.h
        AST.cpp
        AST.h

)