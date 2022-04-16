package com.redcadeted.tenderhack.domain.models

data class DealItem(
    val idDeal: Int,
    val nameDeal: String,
    val descDeal: String,
    val date: Long,
    val ownerId: Int,
    val firstPlace: Int,
    val secondPlace: Int,
    val statusDeal: String,
    val startPrice: String
)