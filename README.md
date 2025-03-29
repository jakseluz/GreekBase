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

