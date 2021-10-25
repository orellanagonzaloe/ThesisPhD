file = ThesisPhD
cmd  = pdflatex
# cmd  = xelatex

src = $(file).tex sections/*.tex include/*.tex bib/*.bib

all: $(file).pdf

$(file).pdf: $(src)
	make clean

	$(cmd) $(file); bibtex $(file) ; $(cmd) $(file) ; $(cmd) $(file) 

	make clean_aux


view:	
	evince $(file).pdf &


clean:
	make clean_aux

	rm -f $(file).pdf


clean_aux:
	rm -f *.aux
	rm -f *.bbl
	rm -f *.blg
	rm -f *.log
	rm -f *.nav
	rm -f *.out
	rm -f *.snm
	rm -f *.toc
	rm -f *.upa
	rm -f *.upb
	rm -f *.vrb
