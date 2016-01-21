Mongolian-Cyrillic language's helper library.

This library written based on 1983's Ts.Damdinsuren, B.Osor's "Монгол үсгийн дүрмийн толь" book. Only official book I can find.

Flaws:
In Rule 9, did not mention its flaw in combined words. Follow up word should be defined by last word from its combination. For example: Батгэрэл, this is people's name. But combined from two different word "Бат", "Гэрэл". So follow up character should be defined by "Гэрэл". And there's no clear cut on splitting combined words without looking at the semantics.
Rule 8, says that male and female characters should not be in same word except combined words. Knowing words gender changes cannot sufficiently express follow up character. Reason:
"Ханбогд", the word is combined but gender changes did not happen. i.e Our algorithm will guess follow up character based on character "а", but in real life people know it was combined word. "Ханбогдоо" is right, "Ханбогдаа" is wrong but our algorithm will use it.

alphabets.py - Alphabets categorized according to rules.
inspector.py - Inspects word features like male, female etc..
validity.py  - Validates Mongolian words. To be Mongolian word, it should satisfy certain conditions like not writing same vowel more than twice.
splitter.py  - Words can be splitted into token like structures.


