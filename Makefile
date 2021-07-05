file = ThesisPhD
cmd  = pdflatex
# cmd  = xelatex

src = $(file).tex sections/*.tex include/*.tex bib/*.bib

all: $(file).pdf

$(file).pdf: $(src)
	make clean
	$(cmd) $(file); bibtex $(file) ; $(cmd) $(file) ; $(cmd) $(file) 
	rm -f *.aux
	rm -f *.log
	rm -f *.nav
	rm -f *.out
	rm -f *.snm
	rm -f *.toc
	rm -f *.vrb
	rm -f *.blg
	rm -f *.bbl

view:	
	evince $(file).pdf &


clean:
	rm -f *.toc
	rm -f *.out
	rm -f *.log
	rm -f *.aux
	rm -f *.blg
	rm -f *.bbl
	rm -f *.nav
	rm -f *.snm
	rm -f *.vrb

	rm -f $(file).pdf

