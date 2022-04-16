package com.redcadeted.tenderhack.ui.extensions

import androidx.lifecycle.Lifecycle
import androidx.lifecycle.LifecycleOwner
import androidx.lifecycle.lifecycleScope
import androidx.lifecycle.repeatOnLifecycle
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.collect
import kotlinx.coroutines.launch

fun <T> Flow<T>.observe(
    lifecycleOwner: LifecycleOwner,
    state: Lifecycle.State = Lifecycle.State.STARTED,
    observer: (T) -> Unit
) {
    with(lifecycleOwner) {
        lifecycleScope.launch {
            repeatOnLifecycle(state) {
                collect { value ->
                    observer(value)
                }
            }
        }
    }
}

data class State<out T>(
    val content: T? = null,
    val loading: Boolean = false,
    val error: Throwable? = null
)

fun <T> stateContent(content: T?): State<T> = State(content = content)

fun <T> stateLoading(content: T? = null): State<T> = State(loading = true, content = content)

fun <T> stateError(error: Throwable, content: T? = null): State<T> =
    State(error = error, content = content)

fun <T> State<T>.processState(
    onLoading: ((T?) -> Unit)? = null,
    onHideLoading: ((T?) -> Unit)? = null,
    onError: (t: Throwable) -> Unit,
    onContent: (T?) -> Unit
) {
    if (loading) {
        onLoading?.invoke(content)
    } else {
        onHideLoading?.invoke(content)
        error?.let { onError(it) } ?: onContent(content)
    }
}