READ ME - Plagiarism Checker



Përshkrimi
Ky projekt është i zhvilluar në Python, i cili përdor algoritmet KMP (Knuth-Morris-Pratt) dhe Rabin-Karp për të krahasuar ngjashmërinë midis dy skedarëve me tekst.
Karakteristikat
•	Lexon dhe pastron tekstet nga karakteret speciale
•	Gjeneron nënvargje për krahasim
•	Përdor KMP dhe Rabin-Karp për kërkimin e modeleve
•	Llogarit përqindjen e ngjashmërisë
•	Mat kohën e ekzekutimit për secilin algoritëm

Kërkesat
•	Python 3.x

Instalimi
Klononi repository-n:
   ```bash
   git clone https://github.com/ElitThaci/PlagiarismChecker.git
   cd PlagiarismChecker
Sigurohuni që keni Python të instaluar.
Ekzekutoni programin:
    python plagiarism_checker.py

Përdorimi
•  Vendosni dy skedarë tekstualë (document1.txt dhe document2.txt) në të njëjtën dosje ku ndodhet skripta.
•  Në plagiarism_checker.py, sigurohuni që emrat e skedarëve janë të sakta:
file1 = 'document1.txt'
file2 = 'document2.txt'
Ekzekutoni programin:
python plagiarism_checker.py
Do të shfaqet përqindja e ngjashmërisë për secilin algoritëm, së bashku me kohën e ekzekutimit.
Shënim: Për dokumente me gjatësi të ndryshme, rekomandohet të përdorni vlera të ndryshme për pattern_length. Për tekste të shkurtra, një pattern_length më i vogël (si 2 ose 3) është më i përshtatshëm, ndërsa për dokumente të gjata mund të përdorni vlera më të mëdha për të rritur saktësinë.

Testimi fillestar
•	Janë kryer teste me tekste të ndryshme me qëllim të kontrollit të korrektësisë së algoritmeve dhe saktësisë në matjen e ngjashmërisë.
•	Testimi është kryer duke ndryshuar gjatësi të nënvargjeve dhe duke provuar tekste me dhe pa ngjashmëri.




Autori
Elit Thaçi
Email: et40413@ubt-uni.net
GitHub: ElitThaci


