max_clauses(100).
enable_recursion.
head_pred(derivationally_related_form,2).
body_pred(instance_hypernym,2).
body_pred(hypernym,2).
body_pred(also_see,2).
body_pred(member_meronym,2).
body_pred(synset_domain_topic_of,2).
body_pred(has_part,2).
body_pred(member_of_domain_usage,2).
body_pred(member_of_domain_region,2).
body_pred(verb_group,2).
body_pred(similar_to,2).
:- discontiguous instance_hypernym/2.
:- discontiguous hypernym/2.
:- discontiguous also_see/2.
:- discontiguous member_meronym/2.
:- discontiguous synset_domain_topic_of/2.
:- discontiguous has_part/2.
:- discontiguous member_of_domain_usage/2.
:- discontiguous member_of_domain_region/2.
:- discontiguous verb_group/2.
:- discontiguous similar_to/2.
