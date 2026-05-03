import logging
from mcp.server.fastmcp import FastMCP

from descriptions import Descriptions
from tarot import Tarot

mcp = FastMCP("tarot", stateless_http=True, streamable_http_path='/tarot-mcp')

tarot = Tarot()

descriptions = Descriptions()

@mcp.tool()
async def get_next_card(withDescription: bool = False) -> str:
    """
    Gets the next card from a shuffled deck
    """
    logging.info("Processing get_next_card")  

    card = tarot.next_card()
    joined_card = ' '.join(card)
    
    if not withDescription:
        return joined_card
    else:
        description = descriptions.getDescription(card[0])
        return f"""
        <card>{joined_card}</card>
        <description>{description}</description>
        """
    

@mcp.tool()
async def reset():
    """
    Shuffle the deck and reset the position
    """
    logging.info("Processing reset")  
    tarot.reset()

@mcp.tool()
async def celtic_cross_next():
    """
    Progress through the Celtic Cross
    """
    logging.info("Processing celtic_cross_next")  
    try:
        card = tarot.next_card() # Type: Card
        position = tarot.next_position()
        description = descriptions.getDescription(card.name)
    except Exception as e:
        logging.error(e)
    return f"""
    <position>{position}</position>
    <card>{card}</card>
    <description>{description}</description>
    """