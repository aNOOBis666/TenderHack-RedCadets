package com.redcadeted.tenderhack.presentation_api.dispatchers

import android.os.Bundle
import androidx.navigation.NavController
import androidx.navigation.NavOptions
import androidx.navigation.Navigator
import dagger.hilt.android.scopes.ActivityRetainedScoped
import kotlinx.coroutines.flow.MutableSharedFlow

@ActivityRetainedScoped
class NavigationDispatcher {
    private val navigationCommandMutableSharedFlow = MutableSharedFlow<NavigationCommand>()

    suspend fun navigate(
        destinationId: Int,
        args: Bundle? = null,
        navOptions: NavOptions? = null,
        navigatorExtras: Navigator.Extras? = null
    ) {
        emit { navController ->
            navController.navigate(destinationId, args, navOptions, navigatorExtras)
        }
    }

    suspend fun back() =
        emit { navController ->
            navController.popBackStack()
        }

    suspend fun backTo(destinationId: Int, inclusive: Boolean = false) {
        emit { navController ->
            navController.popBackStack(destinationId, inclusive)
        }
    }

    private suspend fun emit(command: NavigationCommand) {
        navigationCommandMutableSharedFlow.emit(command)
    }
}

typealias NavigationCommand = (NavController) -> Unit