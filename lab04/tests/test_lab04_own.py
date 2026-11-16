from src.panel import Variant, sorted_copy, sort_variants
from src.lookup import kmer_counts, safe_expression


def test_sorted_copy_keeps_original_unchanged():
    items = [3, 1, 2]

    result = sorted_copy(items)

    assert result == [1, 2, 3]
    assert items == [3, 1, 2]
    assert result is not items


def test_sort_variants_orders_x_and_m_correctly():
    variants = [
        Variant("M", 1, "A", "G"),
        Variant("X", 1, "A", "G"),
        Variant("2", 1, "A", "G"),
        Variant("1", 1, "A", "G"),
    ]

    result = sort_variants(variants)

    assert [v.chrom for v in result] == ["1", "2", "X", "M"]


def test_kmer_counts_k_larger_than_sequence_and_empty_string():
    assert kmer_counts("ATG", 5) == {}
    assert kmer_counts("", 1) == {}


def test_safe_expression_missing_gene_and_zero_value():
    expression = {
        "BRCA1": 8.2,
        "MYC": 0.0,
    }

    assert safe_expression(expression, "TP53") is None
    assert safe_expression(expression, "MYC") == 0.0