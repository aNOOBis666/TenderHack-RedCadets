package com.redcadeted.tenderhack.presentation_api.navigation

import com.redcadeted.tenderhack.R
import com.redcadeted.tenderhack.presentation_api.dispatchers.NavigationDispatcher
import com.redcadeted.tenderhack.ui.dealFragment.DealFragment

class Navigation(
    private val navigationDispatcher: NavigationDispatcher
): INavigation {

    override suspend fun onShowDeal(dealId: Int) {
        navigationDispatcher.navigate(R.id.dealFragment, DealFragment.getArgs(dealId))
    }
}