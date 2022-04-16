package com.redcadeted.tenderhack.ui.dealsListFragment

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.View
import androidx.fragment.app.viewModels
import by.kirich1409.viewbindingdelegate.viewBinding
import com.redcadeted.tenderhack.R
import com.redcadeted.tenderhack.databinding.FragmentDealsListBinding
import com.redcadeted.tenderhack.domain.models.DealItem
import com.redcadeted.tenderhack.ui.dealsListFragment.adapters.DealsAdapter
import com.redcadeted.tenderhack.ui.extensions.State
import com.redcadeted.tenderhack.ui.extensions.observe
import com.redcadeted.tenderhack.ui.extensions.processState
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class DealsListFragment : Fragment(R.layout.fragment_deals_list) {

    private val viewModel: DealsListViewModel by viewModels()
    private val viewBinging by viewBinding(FragmentDealsListBinding::bind)

    private val dealsAdapter = DealsAdapter(::onDealClick)

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        viewModel.onLoadDeals()
        viewBinging.dealsList.adapter = dealsAdapter
        viewModel.dealsEvents.observe(this, observer = ::renderDeals)
    }

    private fun renderDeals(state: State<List<DealItem>>) {
        state.processState(
            onLoading = { renderLoading(true) },
            onHideLoading = { renderLoading(false) },
            onContent = { content -> renderContent(content) },
            onError = {
//                TODO: On error state
            }
        )
    }

    private fun renderLoading(show: Boolean) {
        // TODO: Impl loading screen
    }

    private fun renderContent(content: List<DealItem>?) {
        dealsAdapter.submitList(content)
    }

    private fun onDealClick(item: DealItem) {
        viewModel.onShowDeal(item.idDeal)
    }

}