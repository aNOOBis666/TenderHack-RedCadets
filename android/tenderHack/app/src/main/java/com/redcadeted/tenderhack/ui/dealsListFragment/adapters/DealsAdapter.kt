package com.redcadeted.tenderhack.ui.dealsListFragment.adapters

import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.redcadeted.tenderhack.R
import com.redcadeted.tenderhack.databinding.ViewDealItemBinding
import com.redcadeted.tenderhack.domain.models.DealItem
import com.redcadeted.tenderhack.ui.extensions.inflate

internal class DealsAdapter(
    private val itemClick: (DealItem) -> Unit
) : ListAdapter<DealItem, DealsAdapter.DealViewHolder>(DiffCallback) {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): DealViewHolder {
        val view = parent.inflate(R.layout.view_deal_item)
        val binding = ViewDealItemBinding.bind(view)
        return DealViewHolder(binding, itemClick)
    }

    override fun onBindViewHolder(holder: DealViewHolder, position: Int) {
        getItem(position)?.let { channel ->
            holder.bind(channel)
        }
    }

    inner class DealViewHolder(
        private val viewBinding: ViewDealItemBinding,
        private val onClick: (DealItem) -> Unit,
    ) : RecyclerView.ViewHolder(viewBinding.root) {

        fun bind(item: DealItem) {
            viewBinding.title.text = item.nameDeal
            viewBinding.sessionStatus.text = item.statusDeal
            viewBinding.sessionNum.text = item.idDeal.toString()
            viewBinding.startCostNumber.text = item.startPrice
            viewBinding.root.setOnClickListener { onClick(item) }
        }
    }

    private object DiffCallback : DiffUtil.ItemCallback<DealItem>() {
        override fun areItemsTheSame(
            oldItem: DealItem,
            newItem: DealItem,
        ): Boolean = oldItem.idDeal == newItem.idDeal

        override fun areContentsTheSame(
            oldItem: DealItem,
            newItem: DealItem
        ): Boolean = oldItem == newItem
    }
}