        const replay = () => {
        document.createElement('addreplay').innerHTML="
            <div class="comment-form">
                <h2>Leave a replay</h2>
                <form method="POST" id="replayForm" action="{%url 'replay'%}" onsubmit="makereplay(event)">
                    {% csrf_token %}
                    <div class="form-group">
                        <label for="replaymessage">Message *</label>
                        <textarea id="replaymessage" cols="30" rows="5" name="replayvalue" class="form-control" required></textarea>
                    </div>
                    <input type="hidden" value="{{ comment }}" name="comment">
                    <div class="form-group">
                        <input type="submit" value="Post Replay" class="btn btn-custom">
                    </div>
                </form>
            </div>
        ";
        }



function