# Perl v5.22.1
# Implementation of Longest Common Subsequence in perl


use strict;
use warnings;
sub lcs {
    my ($s1, $s2) = @_;
    if (!length($s1) || !length($s2)) {
        return "";
    }
    if (substr($s1, 0, 1) eq substr($s2, 0, 1)) {
        return substr($s1, 0, 1) . lcs(substr($s1, 1), substr($s2, 1));
    }
    my $a = lcs(substr($s1, 1), $s2) || "";
    my $b = lcs($s1, substr($s2, 1)) || "";
    return length($a) > length($b) ? $a : $b;
}

my $seq = lcs("ATCGGCACTCAT", "ACGTGCAG");
print "Longest Common Subsequence is ",$seq . "\n";

print"Length of Longest Common Subsequence is ",length($seq);