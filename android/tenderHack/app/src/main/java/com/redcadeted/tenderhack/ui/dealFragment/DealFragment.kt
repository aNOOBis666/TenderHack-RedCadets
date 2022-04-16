package com.redcadeted.tenderhack.ui.dealFragment

import android.os.Bundle
import android.view.View
import androidx.fragment.app.Fragment
import androidx.fragment.app.viewModels
import by.kirich1409.viewbindingdelegate.viewBinding
import com.redcadeted.tenderhack.R
import com.redcadeted.tenderhack.databinding.FragmentDealsBinding

class DealFragment: Fragment(R.layout.fragment_deals) {

    companion object{
        private const val CURRENT_DEAL = "current_deal"

        fun getArgs(id: Int): Bundle {
            val args = Bundle()
            args.putInt(CURRENT_DEAL, id)
            return args
        }
    }

    private val viewModel: DealViewModel by viewModels()
    private val viewBinding by viewBinding(FragmentDealsBinding::bind)

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
    }
}