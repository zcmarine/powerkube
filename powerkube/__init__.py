import kubernetes
from powerline.theme import requires_segment_info

_KUBE_SYMBOL = u'\U00002388 '


@requires_segment_info
def context(pl, segment_info, show_cluster=False, show_namespace=True, show_user=False,
            alert_namespaces=()):
    '''
    Return the current kubernetes context items of cluster, namespace, and/or user as separate
    segments. Uses the 'kubernetes_cluster', 'kubernetes_namespace', and 'kubernetes_user'
    highlight groups.

    Because you may not want your kubernetes context in your status bar at all times, you can
    disable it by setting an environment variable 'RENDER_POWERLINE_KUBERNETES' to anything
    other than true. One way to do this would be with a simple function, such as putting this
    in your ~/.bash_profile:

        kshow() {
            if [[ $RENDER_POWERLINE_KUBERNETES = "NO" ]]; then
                export RENDER_POWERLINE_KUBERNETES=YES
            else
                export RENDER_POWERLINE_KUBERNETES=NO
            fi
        }

    Then you can toggle showing your kubernetes context in powerline by just typing `kshow`
    in your terminal
    '''
    pl.debug('Running powerline-kubernetes')

    render_context = segment_info['environ'].get('RENDER_POWERLINE_KUBERNETES', 'YES')
    if render_context != 'YES':
        return []

    try:
        context = kubernetes.K8sConfig().current_context_dict
    except Exception as e:
        pl.error(e)
        return

    if not any([show_cluster, show_namespace, show_user]):
        return []

    segments_list = []

    if show_cluster:
        segments_list.append(
            {'contents': context.get('cluster'),
             'highlight_groups': ['kubernetes_cluster'],
             }
        )

    if show_namespace:
        namespace = context.get('namespace')
        be_alert = namespace in alert_namespaces
        highlight_group = 'kubernetes_namespace:alert' if be_alert else 'kubernetes_namespace'
        segments_list.append(
            {'contents': context.get('namespace'),
             'highlight_groups': [highlight_group],
             }
        )

    if show_user:
        segments_list.append(
            {'contents': context.get('user'),
             'highlight_groups': ['kubernetes_user'],
             }
        )

    # Add the Kubernetes symbol before the first segment
    first_highlight_group = segments_list[0]['highlight_groups']
    segments_list.insert(0, {'contents': _KUBE_SYMBOL,
                             'highlight_groups': first_highlight_group
                             }
                         )
    return segments_list
