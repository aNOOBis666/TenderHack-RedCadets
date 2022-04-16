package com.redcadeted.tenderhack.ui.dealsListFragment

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.redcadeted.tenderhack.domain.models.DealItem
import com.redcadeted.tenderhack.presentation_api.navigation.INavigation
import com.redcadeted.tenderhack.ui.extensions.State
import com.redcadeted.tenderhack.ui.extensions.stateContent
import com.redcadeted.tenderhack.ui.extensions.stateLoading
import dagger.hilt.android.scopes.ViewModelScoped
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

@ViewModelScoped
class DealsListViewModel(
    private val navigate: INavigation
) : ViewModel() {

    private val _dealsEvents = MutableStateFlow<State<List<DealItem>>>(stateLoading())
    val dealsEvents = _dealsEvents.asStateFlow()

    fun onLoadDeals(){
        _dealsEvents.value = stateContent(emptyList())
    }

    fun onShowDeal(dealId: Int){
        viewModelScope.launch {
            navigate.onShowDeal(dealId)
        }
    }
}