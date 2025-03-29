# <span style="color:blue"> GREEK BASE </span>
## Opis projektu:
Własny obiektowy język programowania z operacjami bazodanowymi „GreekBase”
Język obiektowy inspirowany Adą, kompilowany do C lub LLVM, z obsługą typów generycznych, listy dwukierunkowej i biblioteki do operacji na bazach danych.

## 1. Wprowadzenie

### Cel projektu

Celem projektu jest stworzenie eksperymentalnego języka programowania inspirowanego składnią i zasadami języka Ada, który będzie obsługiwał:

- Programowanie obiektowe,
- Typy generyczne,
- Listę dwukierunkową jako wbudowaną strukturę danych,
- Wbudowaną bibliotekę do operacji na bazach danych.

Kompilator języka zostanie zaimplementowany z backendem generującym kod w języku C lub LLVM IR (decyzja zostanie podjęta na dalszym etapie projektu).

## 2. Analiza i projekt języka

### 2.1 Składnia i semantyka

- Wzorowanie się na Adzie w zakresie składni (m.in. bloki `begin ... end`, silne typowanie, kontrakty).
- Klasy i dziedziczenie oparte na zasadach podobnych do Ady.
- Obsługa typów generycznych w stylu Ady (np. `generic type T is private;`).

### 2.2 Struktury danych

- Wbudowana obsługa listy dwukierunkowej:
  - Interfejs listy z metodami `Insert`, `Delete`, `Find`.
  - Obsługa iteratorów dla wygodnej iteracji po elementach.

### 2.3 Operacje na bazach danych

- Biblioteka wbudowana w język do prostych operacji SQL.
- Możliwość wykonywania zapytań przez interfejs wysokopoziomowy.
- Wsparcie dla SQLite jako backendu.

## 3. Implementacja kompilatora

### 3.1 Frontend

#### Analiza leksykalna i składniowa

- Definicja gramatyki języka (BNF/EBNF).
- Implementacja analizatora leksykalnego (np. Flex).
- Implementacja parsera (np. Bison).

#### Analiza semantyczna

- Sprawdzanie typów, reguł obiektowych i poprawności kodu generycznego.
- Obsługa błędów kompilacji z czytelnymi komunikatami.

### 3.2 Backend

- Opcja 1: Generowanie kodu w C.
- Opcja 2: Generowanie LLVM IR dla lepszej optymalizacji.
- Implementacja systemu zarządzania pamięcią (np. ręczne zarządzanie, wsparcie dla prostego GC Do ustalenia).

## 4. Implementacja biblioteki standardowej

- Moduł obsługi listy dwukierunkowej.
- Moduł obsługi baz danych (interfejs do SQLite).
- Moduł wejścia/wyjścia.

## 5. Testowanie i dokumentacja

- Testowanie jednostkowe kompilatora.
- Testowanie wygenerowanego kodu.
- Dokumentacja języka i jego biblioteki.

## 6. Harmonogram

### Etap 1: Projektowanie języka i jego składni&#x20;

### Etap 2: Implementacja frontendu kompilatora&#x20;

### Etap 3: Implementacja backendu kompilatora&#x20;

### Etap 4: Tworzenie biblioteki standardowej&#x20;

### Etap 5: Testowanie i dokumentacja

## 7. Podsumowanie

Projekt zakłada stworzenie nowoczesnego języka programowania z prostą, ale solidną infrastrukturą kompilacyjną. Kluczowe funkcje, takie jak obsługa generyków, listy dwukierunkowej i interfejs do baz danych, uczynią go wygodnym w zastosowaniach praktycznych.

# Szczegóły techniczne projektu

## Lista tokenów - TO DO zrobic żeby bylo bardziej nowoczesne np zaminiec begin end na klamerki

### 1. Słowa kluczowe
```
KW_BEGIN       "begin"
KW_END         "end"
KW_IF          "if"
KW_THEN        "then"
KW_ELSE        "else"
KW_LOOP        "loop"
KW_WHILE       "while"
KW_FOR         "for"
KW_IN          "in"
KW_RETURN      "return"
KW_PROCEDURE   "procedure"
KW_FUNCTION    "function"
KW_IS          "is"
KW_TYPE        "type"
KW_RECORD      "record"
KW_ARRAY       "array"
KW_OF          "of"
KW_VAR         "var"
KW_CONST       "const"
KW_GENERIC     "generic"
KW_PACKAGE     "package"
KW_USE         "use"
KW_WITH        "with"
KW_PRIVATE     "private"
KW_PROTECTED   "protected"
KW_OVERRIDE    "override"
KW_CLASS       "class"
KW_NEW         "new"
```

### 2. Operatory i symbole
```
OP_ASSIGN      ":="
OP_EQUAL       "="
OP_NOT_EQUAL   "/="
OP_LESS        "<"
OP_LESS_EQ     "<="
OP_GREATER     ">"
OP_GREATER_EQ  ">="
OP_PLUS        "+"
OP_MINUS       "-"
OP_MUL         "*"
OP_DIV         "/"
OP_MOD         "mod"
OP_AND         "and"
OP_OR          "or"
OP_NOT         "not"
OP_DOT         "."
OP_COLON       ":"
OP_SEMICOLON   ";"
OP_COMMA       ","
OP_ARROW       "=>"
OP_LPAREN      "("
OP_RPAREN      ")"
OP_LBRACKET    "["
OP_RBRACKET    "]"
```
### 3. Literały
```
LIT_INT        "[0-9]+"
LIT_FLOAT      "[0-9]+\\.[0-9]+"
LIT_STRING     "\"[^\"]*\""
LIT_CHAR       "'[a-zA-Z0-9]'"
```
### 4. Identyfikatory
```
IDENTIFIER     "[a-zA-Z_][a-zA-Z0-9_]*"
```
5. Komentarze
```
COMMENT        "--.*"
MULTILINE_COMMENT  "/* .*? */"
```
