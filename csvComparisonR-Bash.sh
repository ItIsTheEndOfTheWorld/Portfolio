#!/bin/bash

END="y"

until [[ ! $END == "y" ]]
do
	#open the first file
	printf "\n\nWhat CSV file would you like to open? (don't include extension)\n"
	read file1No
	file1="$file1No.csv"
	
	exists="y"
	if [[ -e $file1 ]]
	then
		file1S="$file1No-Sorted.csv" #may not be used. -\_("/)_/-
		sort -t ',' -k1 --version-sort -o $file1S $file1
		echo Sorted $file1
	else
		exists="n"
	fi
	#see if the user wants to open another file (to combine data)
	printf "\nWould you like to combine that file with another CSV file? (type \"y\" or \"n\")\n"
	read second

	if [[ $second == "y" ]]
	then
		printf "\nWhat CSV file would you like to open? (don't include extension)\n"
		read file2No
		file2="$file2No.csv"

		printf "\nWhat would you like the combined file to be called? (don't include extension)"
		read combinedName
		
		#create a file by that name. don't overwrite if already exists, add a number to the end
		filename="$combinedName.csv"
		new="n"
		i=0
		until  [[ $new == "y" ]]
		do
			if [[ -e $filename ]]
			then
				filename="$combinedName$i.csv"
				i=$(($i + 1))
			else
				new="y"
			fi
		done
		
		#make the file to-be-combined in
		touch $filename
		echo Created file $filename

		#sort for easier parsing and combining - make sure the files exist first
		if [[ -e $file2 ]]
		then
			file2S="$file2No-Sorted.csv"
			sort -t ',' -k1 --version-sort -o $file2S $file2
			echo Sorted $file2
		else
			exists="n"
		fi
	
		if [[ $exists == "n" ]]
		then
			echo Sorry, files $file1 and $file2 cannot be combined.
		else

			#actually merge and save the data
			$(join -j 1 -t ',' --nocheck-order -a1 -a2 -o 1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.8,2.9,1.10,1.11 $file1S $file2S > $filename)

			echo Joined files in $filename
		fi
		combo="y"


	else
		if [[ ! -e $file1 ]]
		then
			exists="n"
		fi
		combo="n"
	fi


	#data handling
	if [[ $exists == "y" ]] && [[ $combo == "y" ]]
	then
		#the files start sorted how they're needed here
		code1=$(tail -n +2 $file1 | cut -d',' -f 8 | uniq -c | awk '{printf("\t %s %d\n", $2, $1);}')
		code2=$(tail -n +2 $file2 | cut -d',' -f 8 | uniq -c | awk '{printf("\t%s %d\n", $2, $1);}')
		printf "\nNumber of occurrences of each code in File 1:\n$code1\n\nNumber of occurrences of each code in File2:\n$code2" 

		#remove sorted files
		$(rm $file1S)
		$(rm $file2S)
		printf "\n\nSorted files removed."
	
	elif [[ $exists == "y" ]]
	then
		#the file starts sorted by code
		code=$(tail -n +2 $file1 | cut -d',' -f 8 | uniq -c | awk '{printf("\t%s %d\n", $2, $1); }')	
		printf "\nNumber of occurrences of each code:\n$code"
		
	else
		echo Please try again.
	fi 	

	printf "\n\nWould you like to run the program again? (type \"y\" or \"n\")\n"
	read quit
	END=$quit
done

