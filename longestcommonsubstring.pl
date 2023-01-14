#Perl v5.22.1
# Implentation of Longest Common substrings in perl

use strict ;
use warnings ;

sub longestCommonSubstr {
   my $first = shift ;
   my $second = shift ;
   my %firstsubs = findSubstrings ( $first );
   my %secondsubs = findSubstrings ( $second ) ;
   my @commonsubs ;
   foreach my $subst ( keys %firstsubs ) {
      if ( exists $secondsubs{ $subst } ) {
   push ( @commonsubs , $subst ) ;
      }
   }
   my @sorted = sort { length $b <=> length $a } @commonsubs ;
   return $sorted[0] ;
}

sub findSubstrings {
   my $string = shift ;
   my %substrings ;
   my $l = length $string ;
   for ( my $start = 0 ; $start < $l ; $start++ ) {
      for ( my $howmany = 1 ; $howmany < $l - $start + 1 ; $howmany++) {
   $substrings{substr( $string , $start , $howmany) } = 1 ;
      }
   }
   return %substrings ;
}

my $seq1 = "AAACCGT";
my $seq2 = "AAACTCG";
my $longest = longestCommonSubstr( $seq1 , $seq2) ;

print "The longest common substring of <$seq1> and <$seq2> is $longest \n" ;
print("the length of the longest common substring is ",length($longest))