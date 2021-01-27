import useAxios from 'axios-hooks'
import propTypes from 'prop-types';

// Return [{loading, error, data}, refetch] where data is the full set
// of current participants
export function useParticipants() {
  return useAxios('/api/participants');
}

// Return [{loading, error, participant}], fetching the
// participant by email address.  If the response is a 404,
// the result is [{loading: false, error: null, participant: null}].
export function useParticipantByEmail(email) {
  const [{ loading, error, data: participant }] = useAxios(`/api/participants/by_email?email=${encodeURIComponent(email)}`);
  if (error?.response?.status === 404) {
    return [{ loading: false, error: null, participant: null }];
  }
  return [{ loading, error, participant }];
}

// a propTypes shape describing the data expected from the API
export const participantType = propTypes.shape({
  id: propTypes.number.isRequired,
  full_name: propTypes.string.isRequired,
  email: propTypes.string.isRequired,
  is_mentor: propTypes.bool.isRequired,
  is_learner: propTypes.bool.isRequired,
  manager: propTypes.string.isRequired,
  manager_email: propTypes.string.isRequired,
  time_availability: propTypes.string.isRequired,
  org: propTypes.string.isRequired,
  org_level: propTypes.string.isRequired,
  time_at_org_level: propTypes.string.isRequired,
  learner_interests: propTypes.arrayOf(propTypes.string).isRequired,
  mentor_interests: propTypes.arrayOf(propTypes.string).isRequired,
  track_change: propTypes.string.isRequired,
  org_chart_distance: propTypes.string.isRequired,
  comments: propTypes.string.isRequired,
});
