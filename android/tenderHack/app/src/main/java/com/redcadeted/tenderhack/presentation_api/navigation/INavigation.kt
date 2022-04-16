package com.redcadeted.tenderhack.presentation_api.navigation

interface INavigation {

    suspend fun onShowDeal(dealId: Int)
}