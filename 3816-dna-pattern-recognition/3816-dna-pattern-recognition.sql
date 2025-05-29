# Write your MySQL query statement below
Select sample_id, dna_sequence, species, 
(Case When dna_sequence Like "ATG%" then 1 else 0 end) as has_start, 
(Case When dna_sequence Like "%TAA" or dna_sequence Like "%TAG" or dna_sequence Like "%TGA"then 1 else 0 end) as has_stop, 
(Case When dna_sequence Like "%ATAT%" then 1 else 0 end) as has_atat, 
(Case When dna_sequence Like "%ggg%" then 1 else 0 end) as has_ggg

From Samples 
Order by 1 