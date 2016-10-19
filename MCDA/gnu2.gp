set term wxt size 800,800
set key rmargin
set xlabel 'Execution time criterion weight'
set ylabel 'Accuracy criterion weight'
set zlabel 'Detail'
set size square
plot "<awk '{if($1==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 1',"<awk '{if($2==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 2',"<awk '{if($3==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 3',"<awk '{if($4==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 4',"<awk '{if($5==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 5',"<awk '{if($6==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 6',"<awk '{if($7==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 7',"<awk '{if($8==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 8',"<awk '{if($9==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 9',"<awk '{if($10==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 10',"<awk '{if($11==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 11',"<awk '{if($12==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 12',"<awk '{if($13==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 13',"<awk '{if($14==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 14',"<awk '{if($15==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 15',"<awk '{if($16==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 16',"<awk '{if($17==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 17',"<awk '{if($18==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 18',"<awk '{if($19==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 19',"<awk '{if($20==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 20',"<awk '{if($21==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 21',"<awk '{if($22==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 22',"<awk '{if($23==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 23',"<awk '{if($24==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 24',"<awk '{if($25==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 25',"<awk '{if($26==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 26',"<awk '{if($27==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 27',"<awk '{if($28==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 28',"<awk '{if($29==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 29',"<awk '{if($30==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 30',"<awk '{if($31==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 31',"<awk '{if($32==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 32',"<awk '{if($33==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 33',"<awk '{if($34==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 34',"<awk '{if($35==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 35',"<awk '{if($36==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 36',"<awk '{if($37==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 37',"<awk '{if($38==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 38',"<awk '{if($39==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 39',"<awk '{if($40==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 40',"<awk '{if($41==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 41',"<awk '{if($42==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 42',"<awk '{if($43==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 43',"<awk '{if($44==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 44',"<awk '{if($45==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 45',"<awk '{if($46==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 46',"<awk '{if($47==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 47',"<awk '{if($48==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 48',"<awk '{if($49==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 49',"<awk '{if($50==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 50',"<awk '{if($51==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 51',"<awk '{if($52==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 52',"<awk '{if($53==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 53',"<awk '{if($54==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 54',"<awk '{if($55==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 55',"<awk '{if($56==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 56',"<awk '{if($57==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 57',"<awk '{if($58==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 58',"<awk '{if($59==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 59',"<awk '{if($60==3){print $61,$63}}' TDA_ranks_weights.dat" t 'Rank 60',
pause -1